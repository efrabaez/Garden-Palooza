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
  Game
} from "./GuestPage";


const config = {
  type: Phaser.AUTO,
  parent: 'phaser',
  width: 800,
  height: 600,
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
            <Window id="phaser">
              <Game id="phaser"></Game>
            </Window>
          </Content>
        </Wrap>
      </Container>
    </>
  );
};

export default GuestPage;
