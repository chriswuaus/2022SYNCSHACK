import { SideBarProps } from "./components.types";
import styles from "../styles/SideBar.module.css";
import Vercel from "../public/vercel.svg";
import Butt from "./butt";
import Search from "./search";
import Link from "next/link";

const SideBar = (props: SideBarProps) => {
  return (
    <aside className={styles.aside}>
      <div className={styles.home}>
        <div className={styles.butt}>
          <Butt highlighted={false} link="asdf" />
        </div>
        <div className={styles.search}>
          <Search highlighted={false} link="asdf" />
        </div>
      </div>
    </aside>
  );
};

export default SideBar;
