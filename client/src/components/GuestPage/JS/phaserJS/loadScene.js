import Phaser from 'phaser';
import socket from '../multiplayer'

class LoadScene extends Phaser.Scene
{
    constructor ()
    {
      super("Load");
    }

    preload ()
    {}

    create ()
    {
      var self = this
      socket.once('levelTransfer', function(level) {
        console.log("level should now be" + level);
        self.scene.start('App', { level: level });
      });
    }
}


export default LoadScene;
