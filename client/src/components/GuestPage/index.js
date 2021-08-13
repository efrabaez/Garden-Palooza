import React from "react";
import Phaser from "phaser";
import config from "./JS/phaserJS/game";
import {
  Container,
  Wrap,
  Icon,
  Content,
  Window,
  Game
} from "./GuestPage";

let game = new Phaser.Game(config);

const GuestPage = () => {
  return (
    <>
      <Container>
        <Wrap>
          <Icon to="/">GP</Icon>
          <Content>
            <Window>
              <Game id="phaser"></Game>
            </Window>
          </Content>
        </Wrap>
      </Container>
    </>
  );
};

export default GuestPage;
