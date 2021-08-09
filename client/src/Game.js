import LoadScene from './JS/phaserJS/loadScene';
import MainScene from './JS/phaserJS/mainScene';
import Phaser from 'phaser';

const config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 816,
  height: 624,
  scene: [ LoadScene, MainScene ]
};

const game = new Phaser.Game(config);

function Game() {
  return (
    <div className="Game">
       Game Window
    </div>
  );
}

export default Game;
