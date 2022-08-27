import styles from "../styles/SemesterBlock.module.css"
import { SemesterBlockProps } from "./components.types"
import UnitCard from "./unit_card"

const SemesterBlock = (props: SemesterBlockProps) => {
    return <div className={styles.rounded}>
        {props.cards.map(({ unitCode, unitName, unitRating }) =>
            <div className={styles.coursetile}>
                <UnitCard unitName={unitName} unitCode={unitCode} unitRating={unitRating} />
            </div>)}
    </div>
}

export default SemesterBlock