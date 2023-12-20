--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: handphone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.handphone (
    "Brand" text,
    "Reputasi" text,
    "Antutu_Score" integer,
    "Batery" integer,
    "Harga" integer,
    "Ukuran_Layar" real
);


ALTER TABLE public.handphone OWNER TO postgres;

--
-- Data for Name: handphone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.handphone ("Brand", "Reputasi", "Antutu_Score", "Batery", "Harga", "Ukuran_Layar") FROM stdin;
Realme C11	Terkenal	105251	5000	1600000	6.5
Infinix Note 12	Cukup Terkenal	320986	5000	2800000	6.7
Samsung Galaxy M21	Cukup Terkenal	168633	6000	3000000	6.4
Oppo A16E	Terkenal	110994	5000	1600000	6.52
Vivo Y15S	Cukup Terkenal	890288	5000	2700000	6.51
Realme 9 Pro	Lumayan Terkenal	400261	5000	3200000	6.6
Infinix GT 10	Lumayan Terkenal	678253	5000	3900000	6.67
Infinix Zero 30	Sangat Terkenal	720090	5000	4300000	6.78
Poco F5	Sangat Terkenal	969903	5000	5300000	6.67
Itel S23	Kurang Terkenal	221000	5000	1400000	6.6
\.


--
-- PostgreSQL database dump complete
--

