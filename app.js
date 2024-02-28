import * as THREE from 'https://unpkg.com/three/build/three.module.js';

let camera, scene, renderer;
let geometry, material, cube;

init();
animate();


function init() {
    // Camera, scene, and cube setup remains the same...
    
    // Renderer setup
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

  const ws = new WebSocket('ws://localhost:6789');
  ws.onerror = function(error) {
    console.error("WebSocket error:", error);
};

    ws.onmessage = function(event) {

        const message = JSON.parse(event.data);
        switch(message.gesture) {
            case "zoom_in":
                camera.position.z -= 10; // Adjust values as needed for your scene
                break;
            case "zoom_out":
                camera.position.z += 10; // Adjust values as needed for your scene
                break;
            case "rotate_left":
                cube.rotation.y -= Math.PI / 8; // Rotate left
                break;
            case "rotate_right":
                cube.rotation.y += Math.PI / 8; // Rotate right
                break;
            // Add more cases as needed
        }
        render(); // This call might be intended to be renderer.render(scene, camera);
    };
}



function animate() {
    requestAnimationFrame(animate);

    // Check if cube is defined before attempting to access its properties
    if (cube) {
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;

        renderer.render(scene, camera);
    }
}
function render() {
    renderer.render(scene, camera);
}
