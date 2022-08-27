import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import UnitCard from "../components/unit_card";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <UnitCard unitName="Prog" unitCode="COMP2017" unitRating={5} />
    </div>
  );
};

export default Home;
