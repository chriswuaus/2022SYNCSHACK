import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import SideBar from "../components/side_bar";

import styles from "../styles/Home.module.css";
import DegreeEntry from "../components/degree_entry";
import { useState } from "react";
import { Button } from "@mui/material";
import { DegreeProps } from "../components/components.types";
import Degree from "../components/degree";

const Home: NextPage = () => {
  const [showModal, setShowModal] = useState(false);
  const [degreePlans, setDegreePlans] = useState<DegreeProps[]>([]);
  const addDegree = (degree: DegreeProps) => {
    setDegreePlans([...degreePlans, degree]);
  };
  return (
    <div>
      <SideBar />
      <main className={styles.main}>
        <h1>Hi John!</h1>
        {degreePlans.map((val, index) => (
          <div style={{ padding: 10 }}>
            <Degree
              degreeName={val.degreeName}
              degreeYear={val.degreeYear}
              major={val.major}
              semester={val.semester}
              link={val.link}
            />
          </div>
        ))}
        <Button
          sx={{ m: 1, maxWidth: 200, background: "#86bd33" }}
          variant="contained"
          onClick={() => {
            setShowModal(true);
          }}
        >
          Add degree
        </Button>
        <div
          className={
            styles.modal + (showModal ? " " + styles["modal-show"] : "")
          }
        >
          <button
            className={styles["align-end"] + " " + styles["close-button"]}
            onClick={() => setShowModal(false)}
          >
            <text style={{ fontSize: 40 }}>&times;</text>
          </button>
          <DegreeEntry onAdd={addDegree} />
        </div>
      </main>
    </div>
  );
};

export default Home;
