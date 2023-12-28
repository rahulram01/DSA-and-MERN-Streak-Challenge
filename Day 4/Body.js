import RestaurantCard from "../Components/RestaurantCard";
import RestObj from "../../utils/restObj";
import { useState } from "react";
const Body = () => {
  const [MockData, setMockData] = useState(RestObj);

  return (
    <div className="body">
      <div className="search">
        <input
          className="input"
          type="text"
          placeholder="Enter the food u want.."
        />
      </div>
      <div className="filter">
        <button
          className="filter-btn"
          onClick={() => {
            filteredlist = MockData.filter((user) => user.info.avgRating > 4.0);
            setMockData(filteredlist);
          }}
        >
          High Rating
        </button>
      </div>
      <div className="restaurant-list">
        {MockData.map((user) => (
          <RestaurantCard key={user.info.id} RestCard={user} />
        ))}
      </div>
    </div>
  );
};

export default Body;
