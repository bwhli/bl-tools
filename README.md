# bl-tools (blt)

## Commands

### blt r2 upload

Upload a single file to a Cloudflare R2 bucket.

```
blt r2 upload [OPTIONS] SOURCE_FILE_PATH DESTINATION_FILE_PATH BUCKET_NAME

╭─ Arguments ──────────────────────────────────────────────────────╮
│ *    source_file_path           PATH  [default: None] [required] │
│ *    destination_file_path      PATH  [default: None] [required] │
│ *    bucket_name                TEXT  [default: None] [required] │
╰──────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────╮
│ --endpoint-url       -e      TEXT  [default: None] │
│ --access-key-id      -a      TEXT  [default: None] │
│ --secret-access-key  -s      TEXT  [default: None] │
╰────────────────────────────────────────────────────╯
```