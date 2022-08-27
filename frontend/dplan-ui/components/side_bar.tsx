import { SideBarProps } from "./components.types"
import styles from "../styles/SideBar.module.css"
import Vercel from "../public/vercel.svg"

const Link = ({}) => {
    return <Vercel />
}

const SideBar = (props: SideBarProps) => {
    return <aside className={styles.aside}>
        <Link/>
    </aside>
}

export default SideBar