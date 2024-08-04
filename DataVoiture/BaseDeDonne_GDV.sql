drop database if exists Data_Voitur;
Create DataBase Data_Voiture ;
use Data_Voiture ;
CREATE TABLE Voitures (
    ID_Voiture INT PRIMARY KEY,
    Ville VARCHAR(100),
    Secteur VARCHAR(100),
    Marque VARCHAR(50),
    Modele VARCHAR(50),
    Annee_Modele INT,
    Kilometrage INT,
    Type_Carburant VARCHAR(50),
    Puissance_Fiscale INT,
    Boite_Vitesses VARCHAR(50),
    Nombre_Portes INT,
    Origine VARCHAR(50),
    Premiere_Main BOOLEAN,
    Etat VARCHAR(50),
    Jantes_Aluminium BOOLEAN,
    Airbags BOOLEAN,
    Climatisation BOOLEAN,
    Navigation_GPS BOOLEAN,
    Toit_Ouvrant BOOLEAN,
    Sieges_Cuir BOOLEAN,
    Radar_Recul BOOLEAN,
    Camera_Recul BOOLEAN,
    Vitres_Electriques BOOLEAN,
    ABS BOOLEAN,
    ESP BOOLEAN,
    Regulateur_Vitesse BOOLEAN,
    Limiteur_Vitesse BOOLEAN,
    CD_MP3_Bluetooth BOOLEAN,
    Ordinateur_Bord BOOLEAN,
    Verrouillage_Centralise_Distance BOOLEAN,
    Prix DECIMAL(10, 2)
);

CREATE TABLE Vendeurs (
    ID_vendeur INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(100),
    Prenom VARCHAR(100),
    Age INT,
    Numero_telephone VARCHAR(20),
    Adresse VARCHAR(255),
    Email VARCHAR(100),
    Date_inscription DATE,
    ID_Voiture INT,
    Date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Date_mise_a_jour TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Voiture) REFERENCES voitures(ID_Voiture)
);
CREATE TABLE Acheteurs (
    ID_acheteur INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(100),
    Prenom VARCHAR(100),
    Age INT,
    Numero_telephone VARCHAR(20),
    Adresse VARCHAR(255),
    Email VARCHAR(100),
    Date_inscription DATE,
    ID_Voiture INT,
    FOREIGN KEY (ID_Voiture) REFERENCES voitures(ID_Voiture),
    Date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Date_mise_a_jour TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Employes (
    ID_employe INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(100),
    Prenom VARCHAR(100),
    Age INT,
    Numero_telephone VARCHAR(20),
    Adresse VARCHAR(255),
    Email VARCHAR(100),
    Date_embauche DATE,
    Salaire DECIMAL(10, 2),
    Date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Date_mise_a_jour TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Login_Employes (
    ID_employe INT,
    UserName VARCHAR(50),
    Password VARCHAR(255),
    FOREIGN KEY (ID_employe) REFERENCES Employes(ID_employe)
);

CREATE TABLE Chef_Employes (
    ID_chef INT PRIMARY KEY,
    Nom VARCHAR(50),
    Prenom VARCHAR(50),
    ID_employe INT,
    FOREIGN KEY (ID_employe) REFERENCES Employes(ID_employe)
);

CREATE TABLE Transactions (
    ID_transaction INT PRIMARY KEY AUTO_INCREMENT,
    ID_Voiture INT,
    ID_vendeur INT,
    ID_acheteur INT,
    ID_employe INT,
    Date_transaction DATE,
    Prix_vendu DECIMAL(10, 2),
    Prix_achat DECIMAL(10, 2),
    Type_transaction VARCHAR(50),
    Mode_paiement VARCHAR(50),
    Statut_transaction VARCHAR(50),
    Commentaire TEXT,
    Date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Date_mise_a_jour TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_voiture) REFERENCES voitures(ID_voiture),
    FOREIGN KEY (ID_vendeur) REFERENCES Vendeurs(ID_vendeur),
    FOREIGN KEY (ID_acheteur) REFERENCES Acheteurs(ID_acheteur),
    FOREIGN KEY (ID_employe) REFERENCES Employes(ID_employe)
);

CREATE TABLE Prix (
    ID_prix INT PRIMARY KEY AUTO_INCREMENT,
    ID_voiture INT,
    Prix DECIMAL(10, 2),
    Date DATE,
    FOREIGN KEY (ID_voiture) REFERENCES Voitures(ID_voiture)
);






