import { Child } from "./child.interface";
import { Community } from "./community.interface";

interface Progress {
  workshop: number;
}

export interface TeamWithChildren {
  is_active: boolean;
  last_updated_at: string;
  created_at: string;
  id: number;
  name: string;
  community: Community;
  children: Child[];
  progress: Progress;
}