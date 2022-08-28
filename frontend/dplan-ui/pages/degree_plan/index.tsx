import { data } from "../../public/mock_data"
import SideBar from "../../components/side_bar"
import styles from "../../styles/DegreePlan.module.css"
import UnitCard from "../../components/unit_card"
import SemesterBlock from "../../components/semester_block"

const DegreePlan = () => {

    return (<div>
        <SideBar />
        <main className={styles.main}>
            {data.map((v, i) =>
                <div className={styles.padded}>
                    <h2>Year {Math.floor(i/2) + 1} Semester {i%2 + 1}</h2>
                    <br/>
                    <SemesterBlock cards={v} />
                </div>)}
        </main>
    </div>)

}
export default DegreePlan
