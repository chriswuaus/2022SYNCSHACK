import type { NextPage } from "next";
import UnitCard from "../components/unit_card";
import Plus from "../components/plus";

import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <UnitCard
        unitName="Systems Programming"
        unitCode="COMP2017"
        unitRating={5}
      />
      <Plus />
    </div>
  );
};

export default Home;
