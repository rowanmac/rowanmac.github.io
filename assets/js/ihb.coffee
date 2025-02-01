---
---

copyText = (text) ->
  document.addEventListener 'copy', (e) ->
    e.clipboardData.setData 'text/plain', text
    e.preventDefault()

  document.execCommand 'copy'