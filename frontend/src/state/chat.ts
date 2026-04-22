import { atom } from 'recoil';

import { ICommand } from 'client-types/*';

export interface IAttachment {
  id: string;
  serverId?: string;
  name: string;
  size: number;
  type: string;
  uploadProgress?: number;
  uploaded?: boolean;
  cancel?: () => void;
  remove?: () => void;
  file?: File;
}

export const attachmentsState = atom<IAttachment[]>({
  key: 'Attachments',
  default: []
});

export const persistentCommandState = atom<ICommand | undefined>({
  key: 'PersistentCommand',
  default: undefined
});

export interface IPageIndexProgress {
  step: number;
  total: number;
  percent: number;
  message: string;
  timestamp: number;
}

export const pageindexProgressState = atom<IPageIndexProgress | null>({
  key: 'PageIndexProgress',
  default: null
});
