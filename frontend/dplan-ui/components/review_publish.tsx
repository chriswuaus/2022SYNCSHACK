import styles from "../styles/ReviewPublish.module.css";

const ReviewPublish = () => {
  return (
    <>
      <div>
        <div className={styles.title}>
          <h1 className={styles.header}>My Review</h1>
          <span className={styles.stars}>
            <img width="30px" src="/star-solid.svg"></img>
            <img width="30px" src="/star-solid.svg"></img>
            <img width="30px" src="/star-solid.svg"></img>
            <img width="30px" src="/star-solid.svg"></img>
            <img width="30px" src="/star-solid.svg"></img>
          </span>
        </div>
      </div>
      <input type="text" className={styles.text_entry}></input>
      <div>
        <button className={styles.publish}>PUBLISH</button>
      </div>
    </>
  );
};
export default ReviewPublish;
