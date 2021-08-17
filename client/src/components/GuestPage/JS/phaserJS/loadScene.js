import Phaser from 'phaser';
import socket from '../multiplayer'

class LoadScene extends Phaser.Scene
{
    constructor ()
    {
      super("Load");
    }

    create ()
    {
      var self = this
      socket.emit('gameLoaded', 'ok', (levelJSON) => {
        let levelData = JSON.parse(levelJSON);
        console.log(levelData);
        self.scene.start('Garden', levelData);
      });
    }
}


export default LoadScene;
