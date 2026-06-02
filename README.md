# luci-design

Workspace for the LUCI brand design system.

## Folder structure

```
luci-design/                          ← open this folder in Cursor
└── LUCI Systems Design System/
    ├── index.html                    ← design system hub (start here)
    ├── colors_and_type.css
    ├── preview/
    ├── assets/
    └── ui_kits/
```

## Open the workspace

**Option A (recommended):** **File → Open Workspace from File…** → choose `luci-design.code-workspace` in this folder.

**Option B:** **File → Open Folder…** → select **`luci-design`** (this directory).

## Live preview (chat left, preview right)

Cursor does **not** include “Show Preview” until you install an extension, **or** you use the built-in **Simple Browser** method below.

### Option A — Built-in (no extension)

1. **Terminal → Run Task…** (or `⌘` `Shift` `P` → **Tasks: Run Task**)
2. Choose **Preview: Start local server**
3. `⌘` `Shift` `P` → type **Simple Browser: Show**
4. Enter: `http://localhost:3000/index.html`
5. Drag the Simple Browser tab to the **right** side of the editor.

To stop the server: focus the terminal running the task and press `Ctrl+C`.

### Option B — Live Preview extension

**While working on a specific file** (email template, preview page, microsite, etc.):

1. Open the HTML file you are editing (e.g. `ui_kits/email/email-6-survey.html`)
2. Click **Show Preview** (toolbar) or `⌘` `Shift` `P` → **Live Preview: Show Preview**
3. The preview shows **that file** and refreshes when you save.

**Hub only when you want the full design system browser:**

1. Open `LUCI Systems Design System/index.html`
2. Show Preview — you get the nav + iframe hub.

Preview does not follow you automatically when you switch tabs; click Show Preview again on the new file, or keep the preview open and switch the editor tab (Live Preview usually updates to the active HTML file on save).

### Option C — Your normal browser

1. Run task **Preview: Start local server** (steps 1–2 above)
2. Open **Safari** or **Chrome** and go to: `http://localhost:3000/index.html`
3. Snap the browser window beside Cursor.

The hub loads all `preview/` specimens and UI kits in one split view — use the left nav inside the hub to switch pages.
# review-queue
