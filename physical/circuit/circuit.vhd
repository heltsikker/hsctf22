--------------------------------------------------------------------------------
--! @file circuit.vhd
--! @brief Segment counter
--! @author Joakim Algrøy
--------------------------------------------------------------------------------

-- Libraries
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

--! Entity
entity circuit is 
  port(
    i_clk   : in  std_logic;
    i_sw0   : in  std_logic;
    i_sw1   : in  std_logic;
    i_sw2   : in  std_logic;
    i_sw3   : in  std_logic;
    o_led0  : out std_logic;
    o_led1  : out std_logic;
    o_led2  : out std_logic;
    o_led3  : out std_logic;
    o_segment1_A  : out std_logic;
    o_segment1_B  : out std_logic;
    o_segment1_C  : out std_logic;
    o_segment1_D  : out std_logic;
    o_segment1_E  : out std_logic;
    o_segment1_F  : out std_logic;
    o_segment1_G  : out std_logic;
    o_segment2_A  : out std_logic;
    o_segment2_B  : out std_logic;
    o_segment2_C  : out std_logic;
    o_segment2_D  : out std_logic;
    o_segment2_E  : out std_logic;
    o_segment2_F  : out std_logic;
    o_segment2_G  : out std_logic
  );
end entity circuit;

--! Architecture of circuit 
architecture arch of circuit is
  type t_segment_nums is array(0 to 15) of std_logic_vector(6 downto 0);
  constant seg_nums : t_segment_nums := (
    "1000000", 
    "1111001", 
    "0100100", 
    "0110000", 
    "0011001", 
    "0010010", 
    "0000010", 
    "1111000", 
    "0000000", 
    "0010000",
    "0001000",
    "0000011",
    "1000110",
    "0100001",
    "0000110",
    "0001110"
  );

  constant seg_off : std_logic_vector(6 downto 0) := "1111111";

  type t_flag_arr is array(0 to 59) of integer;
  constant flag : t_flag_arr := (4,8,5,3,4,3,5,4,4,6,7,11,7,9,6,15,7,5,5,15,6,3,6,15,7,5,6,12,6,4,5,15,7,7,6,15,7,2,6,11,5,15,6,1,7,4,5,15,6,9,6,14,7,4,6,5,6,12,7,13);

  type state_t is (
    s_idle,
    s_display
  );

  signal segment1 : std_logic_vector(6 downto 0);
  signal segment2 : std_logic_vector(6 downto 0);
  signal counter  : unsigned(23 downto 0);
  signal ones     : integer range 0 to 9;
  signal tens     : integer range 0 to 9;

  signal show_flag : std_logic;

  signal state : state_t := s_idle;
begin
  pin_dev : entity work.pin
  port map(
    clk => i_clk,
    sw0 => i_sw0,
    sw1 => i_sw1,
    sw2 => i_sw2,
    sw3 => i_sw3,
    show_flag => show_flag
  );

  o_segment1_A <= segment1(0);
  o_segment1_B <= segment1(1);
  o_segment1_C <= segment1(2);
  o_segment1_D <= segment1(3);
  o_segment1_E <= segment1(4);
  o_segment1_F <= segment1(5);
  o_segment1_G <= segment1(6);
  o_segment2_A <= segment2(0);
  o_segment2_B <= segment2(1);
  o_segment2_C <= segment2(2);
  o_segment2_D <= segment2(3);
  o_segment2_E <= segment2(4);
  o_segment2_F <= segment2(5);
  o_segment2_G <= segment2(6);

  o_led0 <= i_sw0;
  o_led1 <= i_sw1;
  o_led2 <= i_sw2;
  o_led3 <= i_sw3;

  p_main: process(i_clk)
    variable flag_count : integer := 0;
  begin
    if rising_edge(i_clk) then
      case state is
        when s_idle =>
          segment1 <= seg_off;
          segment2 <= seg_off;

          if (show_flag = '1') then
            state <= s_display;
            flag_count := 0;
            counter <= to_unsigned(1,24);
          end if;
        when s_display =>
          counter <= counter + 1;

          segment1 <= seg_nums(flag(flag_count));
          segment2 <= seg_nums(flag(flag_count+1));

          if (counter = 0) then
            flag_count := flag_count + 2;
            if (flag_count = 60) then
              counter <= to_unsigned(1,24);
              state <= s_idle;
            end if;
          end if;
      end case;
    end if;
  end process p_main;
end architecture arch;
