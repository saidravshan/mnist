
window.onload = function() {
    let isDrawing = false
    const clear = document.getElementById('clear')
    const submit = document.getElementById('submit')
    const canvas = document.getElementById('canvas')
    const context = canvas.getContext('2d')
    context.strokeStyle = "#333232"
    context.lineWidth = 18

    canvas.addEventListener('mouseup', () => isDrawing = false)
    canvas.addEventListener('mousedown', (e) => {
      isDrawing = true
      context.beginPath()
      context.moveTo(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop)
    })
    canvas.addEventListener('mousemove', (e) => {
       if (!isDrawing) return
       let x = e.pageX - canvas.offsetLeft
       let y = e.pageY - canvas.offsetTop
       context.lineTo(x, y)
       context.stroke()
    })
    clear.addEventListener('click', () => context.clearRect(0, 0, canvas.width, canvas.height))
    submit.addEventListener('click', async () => {
        const array = resize(canvas).data.filter((e, i) => i % 4 === 3)
        const data = Object.values(array)

        submit.classList.add('is-loading')
        post('/predict', { data }).then((data) => {
            submit.classList.remove('is-loading')
            alert("Predictions is:  " + data.prediction)
        })
    })

}

function resize(canvas) {
    const c = document.createElement('canvas')
    const ctx = c.getContext('2d')
    c.height = 28
    c.width = 28
    ctx.scale(0.1, 0.1)
    ctx.drawImage(canvas, 0, 0)
    return ctx.getImageData(0, 0, 28, 28)
}


function post(url, data) {
    return fetch(url, {
        method: 'post',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(response => response.json())
}