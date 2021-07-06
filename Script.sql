CREATE TABLE animais(
	id SERIAL PRIMARY KEY,
	nomeAnimal VARCHAR(255) NOT NULL,
	nomeCientifico VARCHAR(255) NOT NULL,
	imagemUrl VARCHAR(255) NOT NULL,
	nivelPerigo INT
);

INSERT INTO animais (nomeAnimal,nomeCientifico,imagemUrl, nivelPerigo) 
VALUES
	('Água-viva-caixa-australiana','Cubozoa','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos11.jpg',8),
	('Cobra-real','Ophiophagus hannah','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos10.jpg',7),
	('Polvo de anéis azuis','Hapalochlaena','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos9.jpg', 6),
	('Caracol de cone-de-mármore','Conus marmoreus','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos8.jpg', 5),
	('Peixe-pedra','Synanceia verrucosa','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos7.jpg', 6),
	('Escorpião deathstalker','Leiurus quinquestriatus','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos6.jpg', 9),
	('Inland taipan','Oxyuranus microlepidotus','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos5.jpg',8),
	('Aranha armadeira ou aranha-de-banana','Phoneutria','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos4.jpg',9),
	('Rã-dardo-venenoso','Dendrobatidae','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos3.jpg',9),
	('Peixe-balão ou baiacu','Tetraodontidae','https://www.sobiologia.com.br/figuras/Curiosidades/dez_animais_venenosos2.jpg',4);