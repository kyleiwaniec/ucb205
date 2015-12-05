CREATE DATABASE TCOUNT;
\c tcount

--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'Standard public schema';


--
-- Name: plpgsql; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: postgres
--

CREATE PROCEDURAL LANGUAGE plpgsql;


ALTER PROCEDURAL LANGUAGE plpgsql OWNER TO postgres;

SET search_path = public;


--
-- Name: twitter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--
DROP SEQUENCE IF EXISTS id_seq;
CREATE SEQUENCE id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.id_seq OWNER TO postgres;

--
-- Name: twitters; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

DROP TABLE IF EXISTS Tweetwordcount;
CREATE TABLE Tweetwordcount (
    id integer DEFAULT nextval('id_seq'::regclass) NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    word TEXT PRIMARY KEY NOT NULL,    
    count integer NOT NULL
);


ALTER TABLE public.Tweetwordcount OWNER TO postgres;

