import { CLD_URL } from "../../utils/url";

const RestaurantCard = (props) => {
  const { RestCard } = props;
  const { name, locality, areaName, costForTwo, avgRating, cloudinaryImageId } =
    RestCard?.info;
  return (
    <div className="res-card">
      <img src={CLD_URL + cloudinaryImageId} alt="" className="cart1" />
      <h3> {name}</h3>
      <h4>{locality}</h4>
      <h5>{areaName}</h5>
      <h6>{costForTwo}</h6>
      <p>{avgRating}</p>
    </div>
  );
};

export default RestaurantCard;
