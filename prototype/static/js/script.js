const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content')
console.log(csrfToken)
const video = document.getElementById('video')
console.log(modelPath);
Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri(modelPath),
  faceapi.nets.faceLandmark68Net.loadFromUri(modelPath),
  faceapi.nets.faceRecognitionNet.loadFromUri(modelPath),
  faceapi.nets.faceExpressionNet.loadFromUri(modelPath)
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    if(detections[0].expressions.neutral>0.80){
        captureImage(canvas, detections[0].expressions.neutral)
    }
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
  }, 100)
})

function captureImage(canvas, score){
    console.log(score)
}