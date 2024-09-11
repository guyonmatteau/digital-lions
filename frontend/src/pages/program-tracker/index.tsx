import React, { useState, useEffect } from "react";
import getCommunities from "@/api/services/communities/getCommunities";
import LinkCard from "@/components/LinkCard";
import Layout from "@/components/Layout";
import SkeletonLoader from "@/components/SkeletonLoader";
import Badge from "@/components/Badge";
interface Community {
  name: string;
  id: number;
}

const ProgramTrackerCommunityPage: React.FC = () => {
  const breadcrumbs = [{ label: "Program tracker", path: "/program-tracker" }];

  const [communities, setCommunities] = useState<Community[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const fetchCommunities = async () => {
    setIsLoading(true);
    try {
      // Simulate a delay in fetching data
      await new Promise((resolve) => setTimeout(resolve, 300));

      const communitiesData = await getCommunities();
      setCommunities(communitiesData);
    } catch (error) {
      console.error("Failed to fetch communities:", error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchCommunities();
  }, []);

  return (
    <Layout breadcrumbs={breadcrumbs}>
      {isLoading ? (
        <>
          {Array.from({ length: 8 }, (_, i) => (
            <SkeletonLoader key={i} height="104px" type="card" />
          ))}
        </>
      ) : (
        <>
          {communities.map((community) => (
            <LinkCard
              key={community.id}
              title={community.name}
              href={`/program-tracker/${community.id}/teams`}
              state={{ communityName: community.name }}
              className="mb-2"
            >
              <div className="text-sm text-right ">
                <Badge className="mb-2" variant="secondary">3 active teams</Badge>
                <Badge variant="success">10 completed teams</Badge>
              </div>
            </LinkCard>
          ))}
        </>
      )}
    </Layout>
  );
};

export default ProgramTrackerCommunityPage;
