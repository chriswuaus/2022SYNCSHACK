import styles from "../styles/Search.module.css";
import Glass from "../public/magnifying-glass-solid.svg";
import { SearchProps } from "./components.types";

const Search = (props: SearchProps) => {
  let stylesFR = styles.button;
  if (props.highlighted) stylesFR += " " + styles["button-highlighted"];
  return (
    <button className={stylesFR}>
      <Glass />
    </button>
  );
};
export default Search;
