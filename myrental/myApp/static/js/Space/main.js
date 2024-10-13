import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Your Three.js code here...
// Create the scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xeeeeee); // Optional background color

// Create the camera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 2, 5);

// Create the renderer
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add lights
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5).normalize();
scene.add(directionalLight);

// Add orbit controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;

// Load the GLTF model
const loader = new GLTFLoader();

// Load the GLTF model with the correct URL

// Correct URL for loading the GLTF model
loader.load('/static/3D/QQ3D.glb', function (gltf) {
    gltf.scene.scale.set(0.1, 0.1, 0.1); // Adjust scale if necessary
    scene.add(gltf.scene);
}, undefined, function (error) {
    console.error(error);
});


// Animation loop
function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}
animate();