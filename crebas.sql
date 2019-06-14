/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     14.06.2019 16:01:28                          */
/*==============================================================*/


alter table "Film_Ocena"
   drop constraint FK_FILM_OCE_FILM_OCEN_OCENA;

alter table "Film_Ocena"
   drop constraint FK_FILM_OCE_OCENA_FIL_FILM;

alter table "Ocena"
   drop constraint FK_OCENA_UZYTKOWNI_UZYTKOWN;

alter table "OsobaPubliczna_Film"
   drop constraint FK_OSOBAPUB_FILM_OSOB_FILM;

alter table "OsobaPubliczna_Film"
   drop constraint FK_OSOBAPUB_OSOBAPUBL_OSOBAPUB;

alter table "OsobaPubliczna_Ocena"
   drop constraint FK_OSOBAPUB_OCENA_OSO_OSOBAPUB;

alter table "OsobaPubliczna_Ocena"
   drop constraint FK_OSOBAPUB_OSOBAPUBL_OCENA;

drop table "Film" cascade constraints;

drop index "Film_Ocena2_FK";

drop index "Film_Ocena_FK";

drop table "Film_Ocena" cascade constraints;

drop index "Uzytkownik_Ocena_FK";

drop table "Ocena" cascade constraints;

drop table "OsobaPubliczna" cascade constraints;

drop index "OsobaPubliczna_Film2_FK";

drop index "OsobaPubliczna_Film_FK";

drop table "OsobaPubliczna_Film" cascade constraints;

drop index "OsobaPubliczna_Ocena2_FK";

drop index "OsobaPubliczna_Ocena_FK";

drop table "OsobaPubliczna_Ocena" cascade constraints;

drop table "Uzytkownik" cascade constraints;

/*==============================================================*/
/* Table: "Film"                                                */
/*==============================================================*/
create table "Film" 
(
   "dataDodania"        DATE,
   "nazwa"              VARCHAR2(200),
   "idFilmu"            INTEGER              not null,
   "dlugoscTrwania"     INTEGER,
   "cena"               INTEGER,
   constraint PK_FILM primary key ("idFilmu")
);

/*==============================================================*/
/* Table: "Film_Ocena"                                          */
/*==============================================================*/
create table "Film_Ocena" 
(
   "idOceny"            INTEGER              not null,
   "idFilmu"            INTEGER              not null,
   constraint PK_FILM_OCENA primary key ("idOceny", "idFilmu")
);

/*==============================================================*/
/* Index: "Film_Ocena_FK"                                       */
/*==============================================================*/
create index "Film_Ocena_FK" on "Film_Ocena" (
   "idOceny" ASC
);

/*==============================================================*/
/* Index: "Film_Ocena2_FK"                                      */
/*==============================================================*/
create index "Film_Ocena2_FK" on "Film_Ocena" (
   "idFilmu" ASC
);

/*==============================================================*/
/* Table: "Ocena"                                               */
/*==============================================================*/
create table "Ocena" 
(
   "wartoscOceny"       INTEGER,
   "dataWstawienia"     DATE,
   "idOceny"            INTEGER              not null,
   "idUzytkownik"       INTEGER,
   constraint PK_OCENA primary key ("idOceny")
);

/*==============================================================*/
/* Index: "Uzytkownik_Ocena_FK"                                 */
/*==============================================================*/
create index "Uzytkownik_Ocena_FK" on "Ocena" (
   "idUzytkownik" ASC
);

/*==============================================================*/
/* Table: "OsobaPubliczna"                                      */
/*==============================================================*/
create table "OsobaPubliczna" 
(
   "idOsobaPubliczna"   INTEGER              not null,
   "Imie"               VARCHAR2(100),
   "Nazwisko"           VARCHAR2(100),
   "dataUrodzenia"      DATE,
   "zawod"              VARCHAR2(20)         not null,
   constraint PK_OSOBAPUBLICZNA primary key ("idOsobaPubliczna")
);

/*==============================================================*/
/* Table: "OsobaPubliczna_Film"                                 */
/*==============================================================*/
create table "OsobaPubliczna_Film" 
(
   "idFilmu"            INTEGER              not null,
   "idOsobaPubliczna"   INTEGER              not null,
   constraint PK_OSOBAPUBLICZNA_FILM primary key ("idFilmu", "idOsobaPubliczna")
);

/*==============================================================*/
/* Index: "OsobaPubliczna_Film_FK"                              */
/*==============================================================*/
create index "OsobaPubliczna_Film_FK" on "OsobaPubliczna_Film" (
   "idFilmu" ASC
);

/*==============================================================*/
/* Index: "OsobaPubliczna_Film2_FK"                             */
/*==============================================================*/
create index "OsobaPubliczna_Film2_FK" on "OsobaPubliczna_Film" (
   "idOsobaPubliczna" ASC
);

/*==============================================================*/
/* Table: "OsobaPubliczna_Ocena"                                */
/*==============================================================*/
create table "OsobaPubliczna_Ocena" 
(
   "idOceny"            INTEGER              not null,
   "idOsobaPubliczna"   INTEGER              not null,
   constraint PK_OSOBAPUBLICZNA_OCENA primary key ("idOceny", "idOsobaPubliczna")
);

/*==============================================================*/
/* Index: "OsobaPubliczna_Ocena_FK"                             */
/*==============================================================*/
create index "OsobaPubliczna_Ocena_FK" on "OsobaPubliczna_Ocena" (
   "idOceny" ASC
);

/*==============================================================*/
/* Index: "OsobaPubliczna_Ocena2_FK"                            */
/*==============================================================*/
create index "OsobaPubliczna_Ocena2_FK" on "OsobaPubliczna_Ocena" (
   "idOsobaPubliczna" ASC
);

/*==============================================================*/
/* Table: "Uzytkownik"                                          */
/*==============================================================*/
create table "Uzytkownik" 
(
   "idUzytkownik"       INTEGER              not null,
   "Imie"               VARCHAR2(100),
   "Nazwisko"           VARCHAR2(100),
   "dataUrodzenia"      DATE,
   "login"              VARCHAR2(50)         not null,
   "haslo"              VARCHAR2(50)         not null,
   constraint PK_UZYTKOWNIK primary key ("idUzytkownik")
);

alter table "Film_Ocena"
   add constraint FK_FILM_OCE_FILM_OCEN_OCENA foreign key ("idOceny")
      references "Ocena" ("idOceny");

alter table "Film_Ocena"
   add constraint FK_FILM_OCE_OCENA_FIL_FILM foreign key ("idFilmu")
      references "Film" ("idFilmu");

alter table "Ocena"
   add constraint FK_OCENA_UZYTKOWNI_UZYTKOWN foreign key ("idUzytkownik")
      references "Uzytkownik" ("idUzytkownik");

alter table "OsobaPubliczna_Film"
   add constraint FK_OSOBAPUB_FILM_OSOB_FILM foreign key ("idFilmu")
      references "Film" ("idFilmu");

alter table "OsobaPubliczna_Film"
   add constraint FK_OSOBAPUB_OSOBAPUBL_OSOBAPUB foreign key ("idOsobaPubliczna")
      references "OsobaPubliczna" ("idOsobaPubliczna");

alter table "OsobaPubliczna_Ocena"
   add constraint FK_OSOBAPUB_OCENA_OSO_OSOBAPUB foreign key ("idOsobaPubliczna")
      references "OsobaPubliczna" ("idOsobaPubliczna");

alter table "OsobaPubliczna_Ocena"
   add constraint FK_OSOBAPUB_OSOBAPUBL_OCENA foreign key ("idOceny")
      references "Ocena" ("idOceny");

