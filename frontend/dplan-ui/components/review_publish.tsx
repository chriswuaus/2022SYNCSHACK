import styles from "../styles/ReviewPublish.module.css";
import Star from "../public/star-solid.svg";

const ReviewPublish = () => {
  return (
    <>
      <div className={styles.container}>
        <div className={styles.title}>
          <h1 className={styles.header}>My Review</h1>
          <div className={styles.rate_bar}>
            <h2 className={styles.rating}>rating: </h2>
            <div>
              <Star />
              <Star />
              <Star />
              <Star />
              <Star />
            </div>
          </div>
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
