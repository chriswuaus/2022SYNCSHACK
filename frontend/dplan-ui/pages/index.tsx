import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import SideBar from "../components/side_bar";
import UnitCard from "../components/unit_card";
import Plus from "../components/plus";
import ReviewPublish from "../components/review_publish";
import Review from "../components/review";
import Butt from "../components/butt";
import Search from "../components/search";

import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div>
      <SideBar />
      <main className={styles.main}>
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempore
          ullam illum nisi inventore excepturi fugit voluptate modi eveniet sed
          exercitationem quae neque eum vitae, assumenda quibusdam dignissimos
          error. Dolorum corporis, numquam illum libero odio autem porro ea
          perspiciatis quibusdam velit placeat architecto eius magnam
          voluptates, qui nobis rem at inventore tempora reiciendis laudantium
          hic. Nisi eius accusantium architecto illum earum dicta, delectus cum
          sapiente fugiat recusandae facilis aspernatur, ipsum iste? Commodi a
          corrupti, delectus totam molestiae nemo cum ad nisi accusamus quidem
          optio voluptatum eveniet odio ullam. Quae corrupti odit laudantium.
          Neque, voluptas sapiente! Nobis consequuntur vitae quas nisi corporis.
        </p>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis
          dolorem fuga nobis cupiditate. Omnis voluptatem, corrupti eos, tempore
          laudantium ratione atque at obcaecati minima recusandae veritatis
          accusamus dolorem, praesentium eum nobis deserunt consequuntur sint
          corporis qui ea aut dolor. Sapiente alias ipsam, animi nesciunt
          distinctio optio pariatur qui dignissimos, dicta aliquam et natus ex
          totam mollitia. Deleniti culpa, sed repudiandae adipisci aspernatur
          dolor dolorum harum magni. Voluptas est cupiditate, quia
          necessitatibus iusto totam temporibus. Debitis, quisquam dolor. Alias
          exercitationem, dolorem neque autem suscipit praesentium quae et
          molestias cupiditate doloremque excepturi nulla porro adipisci
          nesciunt amet tempora perspiciatis tenetur qui asperiores.
        </p>
        <UnitCard unitName="Prog" unitCode="COMP2017" unitRating={5} />
        <Plus />
        <Review />
        <ReviewPublish />
        {/* <Butt highlighted={true} link="sdfgs" /> */}
        <Search highlighted={true} link="sdfad" />
      </main>
    </div>
  );
};

export default Home;
