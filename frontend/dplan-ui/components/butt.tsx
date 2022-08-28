import styles from "../styles/Butt.module.css";
import House from "../public/house-solid.svg";
import { ButtProps } from "./components.types";
import Link from "next/link";
const Plus = (props: ButtProps) => {
  let stylesFR = styles.button;
  if (props.highlighted) stylesFR += " " + styles["button-highlighted"];
  return (
    <div className={stylesFR}>
      <Link href="/">
        <House />
      </Link>
    </div>
  );
};
export default Plus;
