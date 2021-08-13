import Phaser from 'phaser';
import socket from '../multiplayer'

class LoadScene extends Phaser.Scene
{
    constructor ()
    {
      super({key:"LoadScene"});
    }

    preload(){
    }

    create ()
    {
      var self = this
      socket.once('levelTransfer', function(level) {
        self.game.level = level;
        self.scene.start('Garden', { level });
      });

    }
}


export default LoadScene;
