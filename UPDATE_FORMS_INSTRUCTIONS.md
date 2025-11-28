# Instructions to Update All Service Forms

## Quick Update Required

To enable AJAX form submissions (no page reload), add this line to the `<head>` section of **ALL service form pages**:

```html
<script src="../form-handler.js"></script>
```

## Where to Add

Add it right after the stylesheet link, like this:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Service Name - Byts of Everything</title>
  <link rel="stylesheet" href="../style.css">
  <script src="../form-handler.js"></script>  <!-- ADD THIS LINE -->
  <style>
    ...
```

## Files to Update

### API Integration Services (4 files)
- ✅ `services/enterprise-api.html` (DONE - example)
- ⬜ `services/simple-api.html`
- ⬜ `services/moderate-api.html`
- ⬜ `services/complex-api.html`

### Unit Testing Services (4 files)
- ⬜ `services/unit-basic.html`
- ⬜ `services/unit-intermediate.html`
- ⬜ `services/unit-advanced.html`
- ⬜ `services/unit-enterprise.html`

### Integration Testing Services (4 files)
- ⬜ `services/integration-basic.html`
- ⬜ `services/integration-intermediate.html`
- ⬜ `services/integration-advanced.html`
- ⬜ `services/integration-enterprise.html`

### Software Testing Services (4 files)
- ⬜ `services/software-basic.html`
- ⬜ `services/software-intermediate.html`
- ⬜ `services/software-advanced.html`
- ⬜ `services/software-enterprise.html`

### Custom Services (4 files)
- ⬜ `services/custom-rescue.html`
- ⬜ `services/custom-mvp.html`
- ⬜ `services/custom-ai.html`
- ⬜ `services/custom-devops.html`

### Other Application Forms (if any)
- ⬜ `services/web-application-form.html`
- ⬜ `services/mobile-application.html`
- ⬜ `services/desktop-application.html`

## Alternative: Automated Script

You can use this PowerShell script to add the line automatically to all HTML files:

```powershell
$files = Get-ChildItem -Path "services" -Filter "*.html" -Recurse

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # Check if script tag already exists
    if ($content -notmatch 'form-handler.js') {
        # Add script tag after stylesheet
        $content = $content -replace '(<link rel="stylesheet" href="../style.css">)', '$1`n  <script src="../form-handler.js"></script>'
        
        Set-Content -Path $file.FullName -Value $content
        Write-Host "Updated: $($file.Name)"
    } else {
        Write-Host "Skipped (already has script): $($file.Name)"
    }
}
```

## What This Enables

✅ Forms submit via AJAX without page reload  
✅ Success/error messages appear at top of page  
✅ Form resets automatically on success  
✅ Button shows "Sending..." state during submission  
✅ Email sent to your address automatically  
✅ Customer receives confirmation email  

## Testing

After updating, test by:
1. Fill out a form
2. Click submit
3. You should see a green success message at the top
4. Page should NOT reload
5. Form should clear automatically
6. Check your email for the submission