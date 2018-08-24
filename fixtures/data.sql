--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5 (Debian 10.5-1.pgdg90+1)
-- Dumped by pg_dump version 10.5 (Debian 10.5-1.pgdg90+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: people; Type: TABLE; Schema: public; Owner: teamsdb
--

CREATE TABLE public.people (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    is_team boolean NOT NULL
);


ALTER TABLE public.people OWNER TO teamsdb;

--
-- Name: people_id_seq; Type: SEQUENCE; Schema: public; Owner: teamsdb
--

CREATE SEQUENCE public.people_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.people_id_seq OWNER TO teamsdb;

--
-- Name: people_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: teamsdb
--

ALTER SEQUENCE public.people_id_seq OWNED BY public.people.id;


--
-- Name: person_x_person; Type: TABLE; Schema: public; Owner: teamsdb
--

CREATE TABLE public.person_x_person (
    parent integer,
    child integer
);


ALTER TABLE public.person_x_person OWNER TO teamsdb;

--
-- Name: people id; Type: DEFAULT; Schema: public; Owner: teamsdb
--

ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.people_id_seq'::regclass);


--
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: teamsdb
--

COPY public.people (id, name, is_team) FROM stdin;
1	Alice	f
2	Bob	f
3	Carlos	f
4	Carol	f
5	Charlie	f
6	Chuck	f
7	Dave	f
8	Eve	f
9	Mallory	f
10	Peggy	f
11	Trent	f
12	Victor	f
13	Walter	f
14	The A-Team	t
15	The B-Team	t
16	The C-Team	t
\.


--
-- Data for Name: person_x_person; Type: TABLE DATA; Schema: public; Owner: teamsdb
--

COPY public.person_x_person (parent, child) FROM stdin;
14	1
14	2
14	3
15	10
15	11
15	12
15	2
16	5
16	8
16	1
16	2
16	14
14	16
\.


--
-- Name: people_id_seq; Type: SEQUENCE SET; Schema: public; Owner: teamsdb
--

SELECT pg_catalog.setval('public.people_id_seq', 33, true);


--
-- Name: people people_pkey; Type: CONSTRAINT; Schema: public; Owner: teamsdb
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_pkey PRIMARY KEY (id);


--
-- Name: person_x_person person_x_person_parent_fkey; Type: FK CONSTRAINT; Schema: public; Owner: teamsdb
--

ALTER TABLE ONLY public.person_x_person
    ADD CONSTRAINT person_x_person_parent_fkey FOREIGN KEY (parent) REFERENCES public.people(id);


--
-- Name: person_x_person person_x_person_child_fkey; Type: FK CONSTRAINT; Schema: public; Owner: teamsdb
--

ALTER TABLE ONLY public.person_x_person
    ADD CONSTRAINT person_x_person_child_fkey FOREIGN KEY (child) REFERENCES public.people(id);


--
-- PostgreSQL database dump complete
--

