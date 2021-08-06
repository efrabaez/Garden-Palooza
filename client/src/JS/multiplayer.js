import { io } from "socket.io-client";

let socket = io.connect('http://localhost:5000');

function levelAsync() {
    return new Promise(function(resolve, reject) {
        
    });
}

async function getLevel() {
	let level = await levelAsync()
	return level 
}

export default socket

//socket.on( 'levelTransfer', function( level ) {});

