entity crc32 is 
	port(
		i_data : std_logic_vector(31 downto 0);
		o_crc  : std_logic_vector(31 downto 0)
	);
end entity;

architecture behavioral of crc32 is
	signal d: std_logic_vector(31 downto 0);
	signal c: std_logic_vector(31 downto 0);
begin

  d<= i_data;
  o_crc<= c;
  c(31)=d(31)+c(31)+d(30)+c(30)+d(29)+c(29)+d(28)+c(28)+d(27)+c(27)+d(25)+c(25)+d(24)+c(24)+d(23)+c(23)+d(15)+c(15)+d(11)+c(11)+d(9)+c(9)+d(8)+c(8)+d(5)+c(5)+;
  c(30)=d(30)+c(30)+d(29)+c(29)+d(28)+c(28)+d(27)+c(27)+d(26)+c(26)+d(24)+c(24)+d(23)+c(23)+d(22)+c(22)+d(14)+c(14)+d(10)+c(10)+d(8)+c(8)+d(7)+c(7)+d(4)+c(4)+;
  c(29)=d(31)+c(31)+d(29)+c(29)+d(28)+c(28)+d(27)+c(27)+d(26)+c(26)+d(25)+c(25)+d(23)+c(23)+d(22)+c(22)+d(21)+c(21)+d(13)+c(13)+d(9)+c(9)+d(7)+c(7)+d(6)+c(6)+d(3)+c(3)+;
  c(28)=d(30)+c(30)+d(28)+c(28)+d(27)+c(27)+d(26)+c(26)+d(25)+c(25)+d(24)+c(24)+d(22)+c(22)+d(21)+c(21)+d(20)+c(20)+d(12)+c(12)+d(8)+c(8)+d(6)+c(6)+d(5)+c(5)+d(2)+c(2)+;
  c(27)=d(29)+c(29)+d(27)+c(27)+d(26)+c(26)+d(25)+c(25)+d(24)+c(24)+d(23)+c(23)+d(21)+c(21)+d(20)+c(20)+d(19)+c(19)+d(11)+c(11)+d(7)+c(7)+d(5)+c(5)+d(4)+c(4)+d(1)+c(1)+;
  c(26)=d(31)+c(31)+d(28)+c(28)+d(26)+c(26)+d(25)+c(25)+d(24)+c(24)+d(23)+c(23)+d(22)+c(22)+d(20)+c(20)+d(19)+c(19)+d(18)+c(18)+d(10)+c(10)+d(6)+c(6)+d(4)+c(4)+d(3)+c(3)+d(0)+c(0);
  c(25)=d(31)+c(31)+d(29)+c(29)+d(28)+c(28)+d(22)+c(22)+d(21)+c(21)+d(19)+c(19)+d(18)+c(18)+d(17)+c(17)+d(15)+c(15)+d(11)+c(11)+d(8)+c(8)+d(3)+c(3)+d(2)+c(2)+;
  c(24)=d(30)+c(30)+d(28)+c(28)+d(27)+c(27)+d(21)+c(21)+d(20)+c(20)+d(18)+c(18)+d(17)+c(17)+d(16)+c(16)+d(14)+c(14)+d(10)+c(10)+d(7)+c(7)+d(2)+c(2)+d(1)+c(1)+;
  c(23)=d(31)+c(31)+d(29)+c(29)+d(27)+c(27)+d(26)+c(26)+d(20)+c(20)+d(19)+c(19)+d(17)+c(17)+d(16)+c(16)+d(15)+c(15)+d(13)+c(13)+d(9)+c(9)+d(6)+c(6)+d(1)+c(1)+d(0)+c(0);
  c(22)=d(31)+c(31)+d(29)+c(29)+d(27)+c(27)+d(26)+c(26)+d(24)+c(24)+d(23)+c(23)+d(19)+c(19)+d(18)+c(18)+d(16)+c(16)+d(14)+c(14)+d(12)+c(12)+d(11)+c(11)+d(9)+c(9)+d(0)+c(0);
  c(21)=d(31)+c(31)+d(29)+c(29)+d(27)+c(27)+d(26)+c(26)+d(24)+c(24)+d(22)+c(22)+d(18)+c(18)+d(17)+c(17)+d(13)+c(13)+d(10)+c(10)+d(9)+c(9)+d(5)+c(5)+;
  c(20)=d(30)+c(30)+d(28)+c(28)+d(26)+c(26)+d(25)+c(25)+d(23)+c(23)+d(21)+c(21)+d(17)+c(17)+d(16)+c(16)+d(12)+c(12)+d(9)+c(9)+d(8)+c(8)+d(4)+c(4)+;
  c(19)=d(29)+c(29)+d(27)+c(27)+d(25)+c(25)+d(24)+c(24)+d(22)+c(22)+d(20)+c(20)+d(16)+c(16)+d(15)+c(15)+d(11)+c(11)+d(8)+c(8)+d(7)+c(7)+d(3)+c(3)+;
  c(18)=d(31)+c(31)+d(28)+c(28)+d(26)+c(26)+d(24)+c(24)+d(23)+c(23)+d(21)+c(21)+d(19)+c(19)+d(15)+c(15)+d(14)+c(14)+d(10)+c(10)+d(7)+c(7)+d(6)+c(6)+d(2)+c(2)+;
  c(17)=d(31)+c(31)+d(30)+c(30)+d(27)+c(27)+d(25)+c(25)+d(23)+c(23)+d(22)+c(22)+d(20)+c(20)+d(18)+c(18)+d(14)+c(14)+d(13)+c(13)+d(9)+c(9)+d(6)+c(6)+d(5)+c(5)+d(1)+c(1)+;
  c(16)=d(30)+c(30)+d(29)+c(29)+d(26)+c(26)+d(24)+c(24)+d(22)+c(22)+d(21)+c(21)+d(19)+c(19)+d(17)+c(17)+d(13)+c(13)+d(12)+c(12)+d(8)+c(8)+d(5)+c(5)+d(4)+c(4)+d(0)+c(0);
  c(15)=d(30)+c(30)+d(27)+c(27)+d(24)+c(24)+d(21)+c(21)+d(20)+c(20)+d(18)+c(18)+d(16)+c(16)+d(15)+c(15)+d(12)+c(12)+d(9)+c(9)+d(8)+c(8)+d(7)+c(7)+d(5)+c(5)+d(4)+c(4)+d(3)+c(3)+;
  c(14)=d(29)+c(29)+d(26)+c(26)+d(23)+c(23)+d(20)+c(20)+d(19)+c(19)+d(17)+c(17)+d(15)+c(15)+d(14)+c(14)+d(11)+c(11)+d(8)+c(8)+d(7)+c(7)+d(6)+c(6)+d(4)+c(4)+d(3)+c(3)+d(2)+c(2)+;
  c(13)=d(31)+c(31)+d(28)+c(28)+d(25)+c(25)+d(22)+c(22)+d(19)+c(19)+d(18)+c(18)+d(16)+c(16)+d(14)+c(14)+d(13)+c(13)+d(10)+c(10)+d(7)+c(7)+d(6)+c(6)+d(5)+c(5)+d(3)+c(3)+d(2)+c(2)+d(1)+c(1)+;
  c(12)=d(31)+c(31)+d(30)+c(30)+d(27)+c(27)+d(24)+c(24)+d(21)+c(21)+d(18)+c(18)+d(17)+c(17)+d(15)+c(15)+d(13)+c(13)+d(12)+c(12)+d(9)+c(9)+d(6)+c(6)+d(5)+c(5)+d(4)+c(4)+d(2)+c(2)+d(1)+c(1)+d(0)+c(0);
  c(11)=d(31)+c(31)+d(28)+c(28)+d(27)+c(27)+d(26)+c(26)+d(25)+c(25)+d(24)+c(24)+d(20)+c(20)+d(17)+c(17)+d(16)+c(16)+d(15)+c(15)+d(14)+c(14)+d(12)+c(12)+d(9)+c(9)+d(4)+c(4)+d(3)+c(3)+d(1)+c(1)+d(0)+c(0);
  c(10)=d(31)+c(31)+d(29)+c(29)+d(28)+c(28)+d(26)+c(26)+d(19)+c(19)+d(16)+c(16)+d(14)+c(14)+d(13)+c(13)+d(9)+c(9)+d(5)+c(5)+d(3)+c(3)+d(2)+c(2)+d(0)+c(0);
  c(9)=d(29)+c(29)+d(24)+c(24)+d(23)+c(23)+d(18)+c(18)+d(13)+c(13)+d(12)+c(12)+d(11)+c(11)+d(9)+c(9)+d(5)+c(5)+d(4)+c(4)+d(2)+c(2)+d(1)+c(1)+;
  c(8)=d(31)+c(31)+d(28)+c(28)+d(23)+c(23)+d(22)+c(22)+d(17)+c(17)+d(12)+c(12)+d(11)+c(11)+d(10)+c(10)+d(8)+c(8)+d(4)+c(4)+d(3)+c(3)+d(1)+c(1)+d(0)+c(0);
  c(7)=d(29)+c(29)+d(28)+c(28)+d(25)+c(25)+d(24)+c(24)+d(23)+c(23)+d(22)+c(22)+d(21)+c(21)+d(16)+c(16)+d(15)+c(15)+d(10)+c(10)+d(8)+c(8)+d(7)+c(7)+d(5)+c(5)+d(3)+c(3)+d(2)+c(2)+d(0)+c(0);
  c(6)=d(30)+c(30)+d(29)+c(29)+d(25)+c(25)+d(22)+c(22)+d(21)+c(21)+d(20)+c(20)+d(14)+c(14)+d(11)+c(11)+d(8)+c(8)+d(7)+c(7)+d(6)+c(6)+d(5)+c(5)+d(4)+c(4)+d(2)+c(2)+d(1)+c(1)+;
  c(5)=d(29)+c(29)+d(28)+c(28)+d(24)+c(24)+d(21)+c(21)+d(20)+c(20)+d(19)+c(19)+d(13)+c(13)+d(10)+c(10)+d(7)+c(7)+d(6)+c(6)+d(5)+c(5)+d(4)+c(4)+d(3)+c(3)+d(1)+c(1)+d(0)+c(0);
  c(4)=d(31)+c(31)+d(30)+c(30)+d(29)+c(29)+d(25)+c(25)+d(24)+c(24)+d(20)+c(20)+d(19)+c(19)+d(18)+c(18)+d(15)+c(15)+d(12)+c(12)+d(11)+c(11)+d(8)+c(8)+d(6)+c(6)+d(4)+c(4)+d(3)+c(3)+d(2)+c(2)+d(0)+c(0);
  c(3)=d(31)+c(31)+d(27)+c(27)+d(25)+c(25)+d(19)+c(19)+d(18)+c(18)+d(17)+c(17)+d(15)+c(15)+d(14)+c(14)+d(10)+c(10)+d(9)+c(9)+d(8)+c(8)+d(7)+c(7)+d(3)+c(3)+d(2)+c(2)+d(1)+c(1)+;
  c(2)=d(31)+c(31)+d(30)+c(30)+d(26)+c(26)+d(24)+c(24)+d(18)+c(18)+d(17)+c(17)+d(16)+c(16)+d(14)+c(14)+d(13)+c(13)+d(9)+c(9)+d(8)+c(8)+d(7)+c(7)+d(6)+c(6)+d(2)+c(2)+d(1)+c(1)+d(0)+c(0);
  c(1)=d(28)+c(28)+d(27)+c(27)+d(24)+c(24)+d(17)+c(17)+d(16)+c(16)+d(13)+c(13)+d(12)+c(12)+d(11)+c(11)+d(9)+c(9)+d(7)+c(7)+d(6)+c(6)+d(1)+c(1)+d(0)+c(0);
  c(0)=d(31)+c(31)+d(30)+c(30)+d(29)+c(29)+d(28)+c(28)+d(26)+c(26)+d(25)+c(25)+d(24)+c(24)+d(16)+c(16)+d(12)+c(12)+d(10)+c(10)+d(9)+c(9)+d(6)+c(6)+d(0)+c(0);


end architecture ;