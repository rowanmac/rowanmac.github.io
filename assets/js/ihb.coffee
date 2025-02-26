---
---

    toggleUl = (button) ->
      button.addEventListener "click", ->
        ul = button.nextElementSibling
        return unless ul?.tagName is "UL"

        if ul.style.display == "none"
          ul.style.display = "block"
          button.innerHTML = "▼ Hide Contents"
        else
          ul.style.display = "none"
          button.innerHTML = "► Show Contents"
          
    document.addEventListener "DOMContentLoaded", ->
      buttons = document.querySelectorAll("button.toggleBibList")
      for button in buttons
        if ul?.tagName is "UL"
          ul.style.display = "none"
        toggleUl(button)