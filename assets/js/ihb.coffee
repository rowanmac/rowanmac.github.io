---
---

document.addEventListener "DOMContentLoaded", ->
  copyIcons = document.querySelectorAll ".copyIcon"

  copyIcons.forEach (icon) ->
    icon.addEventListener "click", (event) ->
      event.stopPropagation() # Prevent the click event from bubbling up to the parent
      copyText(event)
      
copyText = (event) ->
  # Your copy text logic here
  alert "Copy icon clicked!"