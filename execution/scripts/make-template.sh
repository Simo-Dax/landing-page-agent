#!/usr/bin/env bash
# make-template.sh — genera una copia PULITA dell'engine, pronta per un nuovo progetto/brand.
# Copia solo l'engine riusabile, esclude segreti e dati personali, e mette placeholder al brand layer.
# Uso:  bash execution/scripts/make-template.sh /percorso/destinazione "Nome Template"
# NON ruota le chiavi: quello è manuale (vedi checklist finale).

set -euo pipefail

SRC="$(cd "$(dirname "$0")/../.." && pwd)"          # root engine
DEST="${1:?Specifica la cartella destinazione}"
NAME="${2:-Landing Page Engine Template}"

echo "Engine sorgente: $SRC"
echo "Destinazione:    $DEST"
mkdir -p "$DEST"

# 1) Copia engine, esclude segreti / personali / build / cache
rsync -a \
  --exclude '.git/' \
  --exclude '.env' \
  --exclude '.env.local' \
  --exclude 'output/' \
  --exclude 'node_modules/' \
  --exclude '.firecrawl/' \
  --exclude '.impeccable/' \
  --exclude '.obsidian/' \
  --exclude '.tmp/' \
  --exclude '.DS_Store' \
  --exclude '.claude/settings.local.json' \
  "$SRC"/ "$DEST"/

# 2) Placeholder al BRAND LAYER (engine resta, identità sparisce)
cat > "$DEST/PRODUCT.md" <<'EOF'
# Product (template)
Compila per il tuo brand: Users (audience/personas), Product Purpose, Brand Personality,
Anti-references, Design Principles, Accessibility. Vedi struttura originale come riferimento.
EOF

cat > "$DEST/DESIGN.md" <<'EOF'
# Design System (template)
Genera con /brand-dna. Frontmatter token (colors/typography/spacing/components) + sezioni 1-7.
EOF

# context/identity e references → svuotati con stub
if [ -d "$DEST/context/identity" ]; then
  rm -f "$DEST/context/identity/"*.md
  cat > "$DEST/context/identity/README.md" <<'EOF'
# Identity (template) — compila per il tuo brand
- tone_of_voice.md
- business_strategy.md
- anti-ai-writing-style.md
EOF
fi
if [ -d "$DEST/context/references" ]; then
  find "$DEST/context/references" -type f ! -name '.gitkeep' -delete 2>/dev/null || true
  touch "$DEST/context/references/.gitkeep"
fi

# 3) .env: solo l'esempio (mai chiavi reali)
rm -f "$DEST/.env"
[ -f "$DEST/.env.example" ] || echo "# copia in .env e compila" > "$DEST/.env.example"

echo "✓ Template creato in: $DEST"
cat <<EOF

── PASSI MANUALI (sicurezza, NON automatizzati) ──
1. RUOTA tutte le chiavi reali (Clerk/Supabase/email tool/Vercel/Firecrawl) dai dashboard.
2. Verifica .mcp.json: solo \${VAR} placeholder (nessun project_ref/URL personale hardcoded).
3. grep di sicurezza nella destinazione:
   grep -rEn 'sk_|pk_live|whsec_|sb_secret|vcp_|eyJ' "$DEST" || echo "nessun segreto trovato ✓"
4. Compila PRODUCT.md, DESIGN.md, context/identity per il nuovo brand (o lancia /setup → /brand-dna).
5. git init nella destinazione SOLO dopo il grep pulito.
EOF
