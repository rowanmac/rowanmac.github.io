---
---

    toggleUl = (button) ->
      button.addEventListener "click", ->
        ul = button.nextElementSibling
        return unless ul?.tagName is "UL"

        if ul.style.display == "none"
          ul.style.display = "block"
        else
          ul.style.display = "none"

    document.addEventListener "DOMContentLoaded", ->
      buttons = document.querySelectorAll("button.toggleBibList")
      for button in buttons
        toggleUl(button)