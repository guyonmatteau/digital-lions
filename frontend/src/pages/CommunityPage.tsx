import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import TextInput from "@/components/TextInput";
import CustomButton from "@/components/CustomButton";
import getCommunities from "@/api/services/communities/getCommunities";
import Loader from "@/components/Loader";
import createCommunity from "@/api/services/communities/createCommunity";
import LinkCard from "@/components/LinkCard";
import { useLocation } from "react-router-dom";
import Breadcrumbs from "@/components/Breadcrumbs";
import Layout from "@/components/Layout";
interface Community {
  name: string;
  id: number;
}

const CommunityPage: React.FC = () => {
  const location = useLocation();
  const breadcrumbs = [{ label: "Communities", path: "/communities" }];

  const [communityName, setCommunityName] = useState("");
  const [communities, setCommunities] = useState<Community[]>([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const fetchCommunities = async () => {
    setLoading(true);
    try {
      const communitiesData = await getCommunities();
      setCommunities(communitiesData);
    } catch (error) {
      console.error("Failed to fetch communities:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCommunities();
  }, []);

  const handleCommunityNameChange = (value: string) => {
    setCommunityName(value);
  };

  const handleCommunityNameBlur = (value: string) => {
    setCommunityName(value);
  };

  const handleAddCommunity = async () => {
    if (communityName.trim() !== "") {
      setLoading(true);
      try {
        const newCommunity = await createCommunity(communityName);
        setCommunities([...communities, newCommunity]);
        setCommunityName(""); // Clear communityName input
      } catch (error) {
        console.error("Error adding community:", error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <Layout breadcrumbs={breadcrumbs}>
      {loading && <Loader loadingText={"Loading communities"} />}

      <TextInput
        className="mb-2"
        label="Community name"
        value={communityName}
        onChange={handleCommunityNameChange}
        onBlur={handleCommunityNameBlur}
      />
      <CustomButton
        label="Add Community"
        onClick={handleAddCommunity}
        variant={"primary"}
        className="hover:bg-card-dark hover:text-white mb-4"
      />
      {communities.map((community) => (
        <LinkCard
          key={community.id}
          title={community.name}
          to={`/communities/${encodeURIComponent(community.id)}/teams`}
          state={{ communityName: community.name }}
          className="mb-2"
        />
      ))}
    </Layout>
  );
};

export default CommunityPage;
