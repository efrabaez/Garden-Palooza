import Phaser from 'phaser';

class TileUI extends Phaser.Scene
{
    constructor ()
    {
      debugger
        super({key: "TileUI"});
    }

    preload ()
    {
      debugger
      this.load.image('button','assets/plantUIButton.png');
      this.load.image('background','assets/plantUIBackground.png');
    }

    create ()
    {
      debugger
      //here I get a json with the plant info
      //this is an example of what would I get from the server
      let jsonExample = {'tileFree': true,'needToWater':false,'needToDisinfect': false}
      this.add.image(430,200,'background');
      
      let plantSomethingButton = this.add.image(20,40,'button');
      plantSomethingButton.setScale(0.3,0.15);
      plantSomethingButton.setOrigin(0,0);
      plantSomethingButton.setInteractive();
      let plantSomethingButtonText = this.add.text(70,85,"   Plant \n Something");
      plantSomethingButtonText.setFontSize(30);

      if( !jsonExample['tileFree'] ){
        plantSomethingButton.visible = false;
        plantSomethingButtonText.visible = false;
      }

      let waterButton = this.add.image(20,250,'button');
      waterButton.setScale(0.3,0.15);
      waterButton.setOrigin(0,0);
      waterButton.setInteractive();
      let waterButtonText = this.add.text(39,306,"Water the Plant");
      waterButtonText.setFontSize(30);

      if( !jsonExample['needToWater'] ){
        waterButton.visible = false;
        waterButtonText.visible = false;
      }

      let removePlant = this.add.image(496,40,'button');
      removePlant.setScale(0.3,0.15);
      removePlant.setOrigin(0,0);
      removePlant.setInteractive();
      let removePlantText = this.add.text(545,90,"Remove Plant");
      removePlantText.setFontSize(30);

      if( jsonExample['tileFree'] ){
        removePlant.visible = false;
        removePlantText.visible = false;
      }

      let disinfectButton = this.add.image(496,250,'button');
      disinfectButton.setScale(0.3,0.15);
      disinfectButton.setOrigin(0,0);
      disinfectButton.setInteractive();
      let disinfectButtonText = this.add.text(515,306,"Disinfect Plant");
      disinfectButtonText.setFontSize(30);

      if( !jsonExample['needToDisinfect'] ){
        disinfectButton.visible = false;
        disinfectButtonText.visible = false;
      }


      let returnButton = this.add.image(250,450,'button');
      returnButton.setScale(0.3,0.15);
      returnButton.setOrigin(0,0);
      returnButton.setInteractive();
      let returnButtonText = this.add.text(240,490,"      Return\n    (Do nothing)");
      returnButtonText.setFontSize(30);
      
      returnButton.on('pointerup', () =>{

            this.scene.stop("TileUI");
            this.scene.start("Garden");
            
       
      });
    }
}



export default TileUI;