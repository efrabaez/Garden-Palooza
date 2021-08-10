import React from "react";
import LoadScene from './JS/phaserJS/loadScene';
import MainScene from './JS/phaserJS/mainScene';
import Phaser from 'phaser';
import {
  Container,
  Wrap,
  Icon,
  Content,
  Window,
} from "./GuestPage";


const config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 600,
  height: 400,
  scene: [ LoadScene, MainScene ]
};

const game = new Phaser.Game(config);

const GuestPage = () => {
  return (
    <>
      <Container>
        <Wrap>
          <Icon to="/">GP</Icon>
          <Content>
            <Window>
             {game}
            </Window>
          </Content>
        </Wrap>
      </Container>
    </>
  );
};

export default GuestPage;
