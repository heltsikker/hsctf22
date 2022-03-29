--------------------------------------------------------------------------------
--! @file pin.vhd
--! @brief Button based "PIN" checker
--! @author Joakim Algrøy
--------------------------------------------------------------------------------

-- Libraries
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

--! Entity
entity pin is 
  port(
    clk   : in std_logic;
    sw0   : in std_logic;
    sw1   : in std_logic;
    sw2   : in std_logic;
    sw3   : in std_logic;
    show_flag : out std_logic
  );
end entity pin;

--! Architecture of pin
architecture arch of pin is
  type state_t is (
    s_idle,
    s_one,
    s_two,
    s_three,
    s_open
  );

  signal state : state_t := s_idle;
begin
  p_main: process(clk)
  begin
    if rising_edge(clk) then
      show_flag <= '0';

      case state is
        when s_idle =>
          if (sw0 = '0' and sw1 = '0' and sw2 = '1' and sw3 = '0') then
            state <= s_one;
          end if;
        when s_one =>
          if (sw0 = '1' and sw1 = '0' and sw2 = '1' and sw3 = '0') then
            state <= s_two;
          end if;
        when s_two => 
          if (sw0 = '1' and sw1 = '1' and sw2 = '1' and sw3 = '0') then
            state <= s_three;
          end if;
        when s_three => 
          if (sw0 = '1' and sw1 = '1' and sw2 = '1' and sw3 = '1') then
            state <= s_open;
            show_flag <= '1';
          end if;
        when s_open =>
          show_flag <= '1';
          state <= s_idle;
      end case;
    end if;
  end process p_main;
end architecture arch;
