import { useRouter } from "next/router";

const UnitPage = () => {
  const router = useRouter();
  const { unit } = router.query;
  return <p>Post{unit}</p>;
};
export default UnitPage;
