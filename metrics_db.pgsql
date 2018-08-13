--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4 (Ubuntu 10.4-0ubuntu0.18.04)
-- Dumped by pg_dump version 10.4 (Ubuntu 10.4-0ubuntu0.18.04)

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
-- Name: deploy_tasks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deploy_tasks (
    id integer NOT NULL,
    task_name character varying(255) NOT NULL,
    time_elapsed character varying(255) NOT NULL,
    date_time timestamp without time zone
);


ALTER TABLE public.deploy_tasks OWNER TO postgres;

--
-- Name: deploy_tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deploy_tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.deploy_tasks_id_seq OWNER TO postgres;

--
-- Name: deploy_tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deploy_tasks_id_seq OWNED BY public.deploy_tasks.id;


--
-- Name: deploy_tasks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deploy_tasks ALTER COLUMN id SET DEFAULT nextval('public.deploy_tasks_id_seq'::regclass);


--
-- Data for Name: deploy_tasks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deploy_tasks (id, task_name, time_elapsed, date_time) FROM stdin;
\.


--
-- Name: deploy_tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deploy_tasks_id_seq', 1, false);


--
-- Name: deploy_tasks deploy_tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deploy_tasks
    ADD CONSTRAINT deploy_tasks_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

