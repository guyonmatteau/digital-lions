import React, { useState } from "react";
import Accordion from "@/components/Accordion";
import CustomButton from "@/components/CustomButton";
import TextInput from "@/components/TextInput";

interface AccordionData {
  title: string;
  description: string;
}

const CommunityPage: React.FC = () => {
  const [communityName, setCommunityName] = useState("");
  const [accordionData, setAccordionData] = useState<AccordionData[]>([]);

  const handleCommunityNameChange = (value: string) => {
    // Optional: Handle community name change if needed
    setCommunityName(value);
  };

  const handleCommunityNameBlur = (value: string) => {
    // Optional: Handle community name blur if needed
    setCommunityName(value);
  };

  const handleAddCommunity = () => {
    // Add new community to accordionData
    if (communityName.trim() !== "") {
      const newAccordionItem: AccordionData = {
        title: communityName,
        description: "Community description placeholder",
      };
      setAccordionData([...accordionData, newAccordionItem]);
      setCommunityName(""); // Clear input after adding community
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">Community Page</h1>
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
        variant={"success"}
      />
      {accordionData.map((item, index) => (
        <Accordion
          key={index}
          title={item.title}
          description={item.description}
        >
          <CustomButton label="add team" variant={"success"} />
        </Accordion>
      ))}
    </div>
  );
};

export default CommunityPage;
