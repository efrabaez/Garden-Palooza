import Phaser from 'phaser';

class Garden extends Phaser.Scene
{
    constructor ()
    {
      super({key: "Garden"});
    }

    init(levelTiles){
      let levelInfo = levelTiles.level;

      this.firstLayer = levelInfo.firstLayer;
      this.secondLayer = levelInfo.secondLayer;
      
    }

    preload ()
    {
      this.load.image("gardenTile","assets/global.png");
    }

    create ()
    {

          
      let map = this.make.tilemap({ data: this.firstLayer, tileWidth: 16, tileHeight: 16 });
      let map2 = this.make.tilemap({ data: this.secondLayer, tileWidth: 16, tileHeight: 16 })
      let tiles = map.addTilesetImage('gardenTile');
      let tiles2 = map2.addTilesetImage('gardenTile');
      let layer = map.createLayer(0, tiles, 0, 0)
      let layer2 = map2.createLayer(0,tiles2,0,0).setInteractive();

      let notValidClickTiles = [2717,2896, 2897, 2898, 2899]


      var self = this;
      layer2.on('pointerup', function (pointer ) {
          let row = Math.floor(pointer.downX);
          let column = Math.floor(pointer.downY);
          let spriteIndex = layer2.getTileAtWorldXY(row,column).index;


          if( !notValidClickTiles.includes(spriteIndex)){
            self.scene.stop('Garden')
            self.scene.start('TileUI', {row: Math.floor(column / 16), column: Math.floor(row / 16), spriteIndex: spriteIndex});
          }
       
      });
    }
}


export default Garden;
