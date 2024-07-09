import { Child } from "./child.interface";
import { Community } from "./community.interface";

export interface TeamWithChildren {
  is_active: boolean;
  name: string;
  id: number;
  children: Child[];
  community: Community;
}