import styles from "../styles/Review.module.css";
import Star from "../public/star-solid.svg";

const Review = () => {
  return (
    <div className={styles.container}>
      <div>
        <div className={styles.title}>
          <h1 className={styles.header}>Riccardo Menon</h1>
          <div>
            <Star />
            <Star />
            <Star />
            <Star />
            <Star />
          </div>
        </div>
      </div>
      <p className={styles.text}>
        The best unit I've ever taken! John Stavrakais is my favourite person.'
      </p>
      <div />
    </div>
  );
};
export default Review;
